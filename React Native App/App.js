import React from 'react';
import ScreenHandler from './src/Components/ScreenHandler'
import {NavigationContainer} from '@react-navigation/native'


/**
 * App where all code is executed
 */
const App = () => {
return(
    <NavigationContainer>
    <ScreenHandler/>
    </NavigationContainer>
    
)

}

export default App;