import NewPasswordForm from "../components/NewPasswordForm";
import styles from "./Page.module.css";

const Page = () => {
  return (
    <div className={styles.page}>
      <div className={styles.content}>
        <NewPasswordForm />
      </div>
      <a className={styles.resetPassword}>Reset Password</a>
    </div>
  );
};

export default Page;
