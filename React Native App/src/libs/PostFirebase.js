import React from 'react';
import database from '@react-native-firebase/database'

const PostFirebase = async(process) => {

const ref = database().ref('/processes/');

await ref.child(`${process}`).set(true).then((response) => {
    console.log(response);
});




}

export default PostFirebase;