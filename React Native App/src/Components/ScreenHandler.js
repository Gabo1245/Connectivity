import React from 'react';
import {createStackNavigator} from '@react-navigation/stack';
import KeyButton from './KeyButton/KeyButton';
import MainMenu from './Main Menu/MainMenu'

const Stack = createStackNavigator();

const ScreenHandler = () => {

return(
    <Stack.Navigator>
        <Stack.Screen name = "KeyButton" component = {KeyButton} options = {{headerShown: false}}/>
        <Stack.Screen name = "MainMenu" component = {MainMenu} options = {{headerShown: false}}/>
    </Stack.Navigator>
)

}

export default ScreenHandler;
