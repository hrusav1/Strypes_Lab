import AuthButtons from "../components/AuthButtons";
import styles from "./Root5.module.css";

const Root5 = () => {
  return (
    <div className={styles.root}>
      <div className={styles.authButtonsWrapper}>
        <AuthButtons />
      </div>
      <a className={styles.home}>Home</a>
    </div>
  );
};

export default Root5;
