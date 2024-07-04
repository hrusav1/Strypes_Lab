import Content1 from "../components/Content1";
import styles from "./Root6.module.css";

const Root6 = () => {
  return (
    <div className={styles.root}>
      <div className={styles.main}>
        <Content1 />
      </div>
      <a className={styles.login}>Login</a>
    </div>
  );
};

export default Root6;
