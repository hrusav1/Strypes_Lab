import FormContainer from "../components/FormContainer";
import styles from "./Root10.module.css";

const Root10 = () => {
  return (
    <div className={styles.root}>
      <div className={styles.content}>
        <FormContainer />
      </div>
      <a className={styles.register}>Register</a>
    </div>
  );
};

export default Root10;
