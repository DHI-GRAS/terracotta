import React, { FC, useState, useEffect } from 'react';
import { Box } from "@material-ui/core"
import { makeStyles } from "@material-ui/core/styles"
import SidebarControl from "./sidebar/SidebarControl"
import SidebarContent from "./sidebar/SidebarContent"
import SidebarTitle from "./sidebar/SidebarTitle"
import SidebarDatasetsItem from "./sidebar-datasets/SidebarDatasetsItem"
import DatasetsColormap from "./colormap/DatasetsColormap"
import Map from "./map/Map"
import { FlyToInterpolator } from 'react-map-gl'
import { easeCubicInOut } from 'd3-ease'
import AppContext, { activeRGBSelectorRange } from "./AppContext"
import { Viewport } from "./map/types"
import { FeatureDataset } from "./map/types"
import { ResponseMetadata200 } from './common/data/getData';
import COLORMAPS, { Colormap } from "./colormap/colormaps"

const useStyles = makeStyles(() => ({
  root: {
    width: '100%',
		height: "100vh",
		margin: 0,
		padding: 0,
  }
}))

const details = 'This applet lets you explore the data on any running Terracotta server. Just search for a dataset to get started!'

const defaultColormap = COLORMAPS[0]

const defaultViewport = {
  latitude: 10.394947325803054,
	longitude: 8.5887344355014,
	zoom: 5.63,
	bearing: 0,
	pitch: 0,
	transitionDuration: 2000,
	transitionInterpolator: new FlyToInterpolator(),
	transitionEasing: easeCubicInOut,
}

const App: FC = () => {
  const [ isSidebarOpen, setIsSidebarOpen ] = useState<boolean>(true)
  const [ viewport, setViewport ] = useState<Viewport>(defaultViewport)
  const [ isOpticalBasemap, setIsOpticalBasemap ] = useState<boolean>(false)

  const [ page, setPage ] = useState<number>(0)
  const [ limit, setLimit ] = useState<number>(15)
  const [ hostname, setHostname ] = useState<string | undefined>(undefined)
  const [ keys, setKeys ] = useState<string[] | undefined>(undefined)
  const [ datasets, setDatasets ] = useState<ResponseMetadata200[] | undefined>(undefined)
  const [ activeDataset, setActiveDataset ] = useState<number | undefined>(undefined)
  const [ hoveredDataset,  setHoveredDataset ] = useState<FeatureDataset | undefined>(undefined)
  const [ selectedDatasetRasterUrl, setSelectedDatasetRasterUrl ] = useState<string | undefined>(undefined)
  const [ colormap, setColormap ] = useState<Colormap>(defaultColormap)
  const [ activeSinglebandRange, setActiveSinglebandRange ] = useState<[number, number] | undefined>(undefined)
  const [ activeEndpoint, setActiveEndpoint ] = useState<string>('singleband')
  const [ activeRGB, setActiveRGB ] = useState<activeRGBSelectorRange | undefined>(undefined)
  const [ datasetBands, setDatasetBands ] = useState<string[] | undefined>(undefined)

  const classes = useStyles(); 

	const toggleSidebarOpen = () => setIsSidebarOpen(!isSidebarOpen)

  function initializeApp(hostname: string) {
    // sanitize hostname
    if (hostname.charAt(hostname.length - 1) === '/') {
        hostname = hostname.slice(0, hostname.length - 1);
    }
    setHostname(hostname)
    
}

  useEffect(() => {
    // window.onload = initializeApp.bind(null, '{{ hostname }}');
    window.onload = initializeApp.bind(null, 'https://oupqp5gj9b.execute-api.eu-central-1.amazonaws.com/development');
  }, [])

  return (
    <div className={classes.root}>
      <AppContext.Provider value={{
        state: {
          isOpticalBasemap,
          viewport,
          hostname,
          keys,
          hoveredDataset,
          datasets,
          activeDataset,
          selectedDatasetRasterUrl,
          page,
          limit,
          colormap,
          activeSinglebandRange,
          activeEndpoint,
          activeRGB,
          datasetBands
        },
        actions: {
          setIsOpticalBasemap,
          setViewport,
          setKeys,
          setHoveredDataset,
          setDatasets,
          setActiveDataset,
          setSelectedDatasetRasterUrl,
          setPage,
          setLimit,
          setColormap,
          setActiveSinglebandRange,
          setActiveEndpoint,
          setActiveRGB,
          setDatasetBands
        }
      }}>
        <Box
          display={'flex'}
          height={1}
          width={1}
        >
          <Map host={hostname}/>
          {isSidebarOpen && (
            <SidebarContent>
              <SidebarTitle
                host={hostname}
                details={details}
                keys={keys}
              />
              {
                hostname && (
                    <SidebarDatasetsItem host={hostname} />
                )
              }
              
            </SidebarContent>
            )}
            <SidebarControl
              toggleSidebarOpen={toggleSidebarOpen}
              isSidebarOpen={isSidebarOpen}
            />
        </Box>
      </AppContext.Provider>
    </div>
   );
}

export default App;