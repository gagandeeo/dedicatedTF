import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import BottomDeck from './components/BottomDeck';
import UpperDeck from './components/UpperDeck';
export default function App() {
  return (
      <LinearGradient
        colors={["#FFB6AD","#FFB6AD", "#679088","#679088", "#245073", "#245073","#FCECD3", "#FCECD3"]}
        style={styles.container}
        locations={[0, 0.35, 0.35, 0.70, 0.70, 0.9, 0.9, 1]}
        start={[0,0.7]}
        end={[1,0.4]}
      >
        <UpperDeck/>
        <BottomDeck/>
      </LinearGradient>
  );
}

const styles = StyleSheet.create({

  container: {
    width: "100%",
    height: "100%"
  },
});
