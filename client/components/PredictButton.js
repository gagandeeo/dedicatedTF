import { Button } from "@rneui/themed";
import { StyleSheet} from 'react-native';
export default function PredictButton() {
  return (
    <Button titleStyle={{color: "black", fontWeight: "bold", fontFamily: "monospace"}} containerStyle={styles.upload__container}
     buttonStyle={styles.upload__button} >
      Detect  
    </Button>
  );
}

const styles = StyleSheet.create({
    upload__container:{
      width: "70%",
      alignSelf: "center",
      borderRadius: 10
    },
    upload__button:{
      padding: 15,
      borderRadius: 10,
      backgroundColor: "#DEE2EE",
      borderWidth: 1,
      borderStyle: "solid",
      borderColor: "#EEEADE",
      opacity: 0.8,
    }
});