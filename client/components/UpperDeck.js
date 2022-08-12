import { StyleSheet, View, Text} from 'react-native';
import Logo from './Logo';
import PredictButton from './PredictButton';
export default function UpperDeck() {
  return (
    <View style={styles.upper__container}>
        <Logo/>
    </View>
  );
}

const styles = StyleSheet.create({
    upper__container:{
        display: 'flex',
        flex: 0.25,
        // backgroundColor: "grey",
        top: "25%",
        justifyContent: "center"
    }
});