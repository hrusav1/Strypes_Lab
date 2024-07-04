import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import PropTypes from "prop-types";
import styles from "./AnalyticsButton1.module.css";

const AnalyticsButton1 = ({
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
      <h1 className={styles.analytics}>{analytics}</h1>
      <img
        className={styles.analyticsGraphStreamlineUlIcon}
        loading="lazy"
        alt=""
        src={analyticsGraphStreamlineU}
      />
    </div>
  );
};

AnalyticsButton1.propTypes = {
  className: PropTypes.string,
  analytics: PropTypes.string,
  analyticsGraphStreamlineU: PropTypes.string,

  /** Action props */
  onAnalyticsButtonContainerClick: PropTypes.func,
};

export default AnalyticsButton1;
