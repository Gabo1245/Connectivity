import React from 'react';
import {View, StyleSheet, TouchableOpacity, Image} from 'react-native';
import {heightPercentageToDP, widthPercentageToDP} from 'react-native-responsive-screen';
import {RFValue} from 'react-native-responsive-fontsize'
import Sound from 'react-native-sound'

const KeyButton = ({navigation}) => {

    var ButtonSound = new Sound("buttonsound.mp3", Sound.MAIN_BUNDLE)
    ButtonSound.setVolume(1)
    const HandlePress = () => {
        ButtonSound.play((response) => {
            
            console.log(response);
            navigation.navigate("MainMenu");

        })
    }

    return (
        <View style = {styles.container}>
            <TouchableOpacity style = {styles.startbutton} onPress = {HandlePress}>
                <Image source = {require('../../Assets/REDALARM.jpg')} style = {styles.buttonimage} />
            </TouchableOpacity>
        </View>

    )
}


const styles = StyleSheet.create({

container: {
    flex: 4,
    backgroundColor: '#212121',
    justifyContent: 'center'

},

startbutton: {

    justifyContent: 'center',
    borderRadius: heightPercentageToDP('5%'),
    
},
buttonimage: {
    width: widthPercentageToDP('30%'),
    height: heightPercentageToDP('20%'),
    alignSelf: 'center'
}



})

export default KeyButton;

