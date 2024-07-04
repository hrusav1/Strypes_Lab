import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import PropTypes from "prop-types";
import styles from "./AuthButtons.module.css";

const AuthButtons = ({ className = "" }) => {
  const navigate = useNavigate();

  const onLoginButtonContainerClick = useCallback(() => {
    navigate("/login-frame");
  }, [navigate]);

  const onRegisterButtonClick = useCallback(() => {
    navigate("/register-frame");
  }, [navigate]);

  return (
    <div className={[styles.authButtons, className].join(" ")}>
      <div className={styles.homeForm} />
      <div className={styles.loginButton} onClick={onLoginButtonContainerClick}>
        <div className={styles.button}>
          <div className={styles.button1} />
          <div className={styles.alreadyAUser}>Already a User</div>
        </div>
      </div>
      <button className={styles.registerButton} onClick={onRegisterButtonClick}>
        <div className={styles.button2}>
          <div className={styles.button3} />
          <div className={styles.register}>Register</div>
        </div>
      </button>
    </div>
  );
};

AuthButtons.propTypes = {
  className: PropTypes.string,
};

export default AuthButtons;
