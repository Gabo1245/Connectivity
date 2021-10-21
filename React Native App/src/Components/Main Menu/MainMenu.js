import React from 'react';
import {View, StyleSheet, Image, TouchableOpacity, Text} from 'react-native';
import {widthPercentageToDP, heightPercentageToDP} from 'react-native-responsive-screen';
import {RFValue} from 'react-native-responsive-fontsize';
import PostFirebase from '../../libs/PostFirebase'

const MainMenu = () => {

const HandlePost = (process) => {

PostFirebase(process);

}

return(

    <View style = {styles.container}>
        
            <View style = {styles.row}>
                <View style = {styles.column}>
                    <Text style = {styles.buttxt}>
                        Rick Roll
                    </Text>
                    <TouchableOpacity style = {styles.button} onPress = {() => {HandlePost("rickroll")}}/>
                </View>
                <View style = {styles.column}>
                    <Text style = {styles.buttxt}>
                        Infinite Errors
                    </Text>
                    <TouchableOpacity style = {styles.button} onPress = {() => {HandlePost("infinite-errors")}}/>
                </View>

            </View>

            <View style = {styles.row}>
                <View style = {styles.column}>
                    <Text style = {styles.buttxt}>
                        Blue Screen
                    </Text>
                    <TouchableOpacity style = {styles.bluebutton} onPress = {() => {HandlePost("blue-screen")}}/>
                </View>
                <View style = {styles.column}>
                    <Text style = {styles.buttxt}>
                        Infinite CMDS
                    </Text>
                    <TouchableOpacity style = {styles.button} onPress = {() => {HandlePost("infinite-cmd")}}/>
                </View>

            </View>
    </View>
);

}

export default MainMenu;

const styles = StyleSheet.create({
    container: {
        flex: 4,
        backgroundColor: '#212121',
        justifyContent: 'center',
        alignContent: 'center'
    
    },

    button: {

        width: widthPercentageToDP('40%'),
        height: heightPercentageToDP('22%'),
        borderRadius: heightPercentageToDP('100%'),
        backgroundColor: '#ff4f4f',
        alignSelf: 'center'

    },

    bluebutton : {
        backgroundColor: '#5b4fff',
        width: widthPercentageToDP('40%'),
        height: heightPercentageToDP('22%'),
        borderRadius: heightPercentageToDP('100%'),
        alignSelf: 'center'
    },

    row: {
        flexDirection: 'row',
        justifyContent: 'space-between'
    },
    
    column: {
        flexDirection: 'column'
    },
    buttxt: {
        fontWeight: 'bold',
        fontSize: RFValue(20),
        color: 'white',
        alignSelf: 'center'
    }

    
    
   
    
})