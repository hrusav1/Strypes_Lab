import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import PropTypes from "prop-types";
import styles from "./Navigation.module.css";

const Navigation = ({ className = "", login }) => {
  const navigate = useNavigate();

  const onResetButtonContainerClick = useCallback(() => {
    navigate("/login-frame");
  }, [navigate]);

  const onReturnButtonContainerClick = useCallback(() => {
    navigate("/home-frame");
  }, [navigate]);

  return (
    <div className={[styles.navigation, className].join(" ")}>
      <div className={styles.buttons}>
        <div
          className={styles.resetButton}
          onClick={onResetButtonContainerClick}
        >
          <div className={styles.button}>
            <div className={styles.button1} />
            <div className={styles.login}>{login}</div>
          </div>
        </div>
        <div
          className={styles.returnButton}
          onClick={onReturnButtonContainerClick}
        >
          <div className={styles.button2} />
          <div className={styles.home}>Home</div>
        </div>
      </div>
    </div>
  );
};

Navigation.propTypes = {
  className: PropTypes.string,
  login: PropTypes.string,
};

export default Navigation;
