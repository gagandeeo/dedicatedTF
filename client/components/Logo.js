import { Image } from "@rneui/themed";
import { StyleSheet, View, Text} from 'react-native';
import SVGImg from "../assets/logo2.svg";
export default function Logo() {
  return (
    // <Image source={{ uri:  }} />
    <View style={styles.logo}>
        <View style={styles.upload__holder}>
            <SVGImg />
            <Text style={styles.upload__text}>Upload</Text> 
        </View>
    </View>
  );
}

const styles = StyleSheet.create({
    logo: {
        alignSelf: "center"
    },
    upload__holder:{
        backgroundColor: "#ffffff",
        alignItems: "center",
        width: 132,
        alignSelf: "ce"
    },
    upload__text: {
        backgroundColor: "#ffffff"
    }
});