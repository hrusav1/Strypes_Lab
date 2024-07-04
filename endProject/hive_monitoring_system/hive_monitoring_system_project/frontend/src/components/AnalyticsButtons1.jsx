import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import PropTypes from "prop-types";
import styles from "./AnalyticsButtons1.module.css";

const AnalyticsButtons1 = ({ className = "", onProfileButtonClick }) => {
  const navigate = useNavigate();

  const onProfileButtonClick1 = useCallback(() => {
    navigate("/profile-frame");
  }, [navigate]);

  return (
    <div className={[styles.analyticsButtons, className].join(" ")}>
      <button className={styles.profileButton} onClick={onProfileButtonClick}>
        <div className={styles.button} />
        <div className={styles.profile}>Profile</div>
        <img
          className={styles.userProfileFocusStreamlineIcon}
          alt=""
          src="/userprofilefocusstreamlinecoreremixpng@2x.png"
        />
      </button>
    </div>
  );
};

AnalyticsButtons1.propTypes = {
  className: PropTypes.string,

  /** Action props */
  onProfileButtonClick: PropTypes.func,
};

export default AnalyticsButtons1;
