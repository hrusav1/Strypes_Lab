import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import PropTypes from "prop-types";
import styles from "./AnalyticsButton.module.css";

const AnalyticsButton = ({
  className = "",
  analytics,
  analyticsGraphStreamlineU,
  onAnalyticsButtonContainerClick,
}) => {
  const navigate = useNavigate();

  const onAnalyticsButtonContainerClick1 = useCallback(() => {
    navigate("/analytics-frame");
  }, [navigate]);

  return (
    <div
      className={[styles.analyticsButton, className].join(" ")}
      onClick={onAnalyticsButtonContainerClick}
    >
      <div className={styles.button} />
      <div className={styles.analytics}>{analytics}</div>
      <img
        className={styles.analyticsGraphStreamlineUlIcon}
        loading="lazy"
        alt=""
        src={analyticsGraphStreamlineU}
      />
    </div>
  );
};

AnalyticsButton.propTypes = {
  className: PropTypes.string,
  analytics: PropTypes.string,
  analyticsGraphStreamlineU: PropTypes.string,

  /** Action props */
  onAnalyticsButtonContainerClick: PropTypes.func,
};

export default AnalyticsButton;
