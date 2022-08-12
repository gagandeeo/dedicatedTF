import { StyleSheet, View, Text} from 'react-native';
import PredictButton from './PredictButton';
export default function BottomDeck() {
  return (
    <View style={styles.bottom__container}>
        <PredictButton/>
        {/* <Text>Hello</Text> */}
    </View>
  );
}

const styles = StyleSheet.create({
    bottom__container:{
        display: 'flex',
        flex: 0.2,
        top: "40%",
        justifyContent: "center",
        borderRadius: 10
    }
});