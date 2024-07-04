import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import PropTypes from "prop-types";
import styles from "./AnalyticsButtons.module.css";

const AnalyticsButtons = ({
  className = "",
  apiary,
  honeyCombStreamlineCyberp,
  onApiaryButtonContainerClick,
}) => {
  const navigate = useNavigate();

  const onApiaryButtonContainerClick1 = useCallback(() => {
    navigate("/apiary-frame");
  }, [navigate]);

  return (
    <div className={[styles.analyticsButtons, className].join(" ")}>
      <div
        className={styles.apiaryButton}
        onClick={onApiaryButtonContainerClick}
      >
        <div className={styles.button} />
        <div className={styles.apiary}>{apiary}</div>
        <img
          className={styles.honeyCombStreamlineCyberpIcon}
          loading="lazy"
          alt=""
          src={honeyCombStreamlineCyberp}
        />
      </div>
    </div>
  );
};

AnalyticsButtons.propTypes = {
  className: PropTypes.string,
  apiary: PropTypes.string,
  honeyCombStreamlineCyberp: PropTypes.string,

  /** Action props */
  onApiaryButtonContainerClick: PropTypes.func,
};

export default AnalyticsButtons;
