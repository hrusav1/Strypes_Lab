import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import PropTypes from "prop-types";
import styles from "./Content.module.css";

const Content = ({ className = "", onHive1ImageClick }) => {
  const navigate = useNavigate();

  const onDashboardButtonContainerClick = useCallback(() => {
    navigate("/dashboard-frame");
  }, [navigate]);

  return (
    <div className={[styles.content, className].join(" ")}>
      <div className={styles.hive1Wrapper}>
        <img
          className={styles.hive1Icon}
          loading="lazy"
          alt=""
          src="/hive-1@2x.png"
          onClick={onHive1ImageClick}
        />
      </div>
      <div
        className={styles.dashboardButton}
        onClick={onDashboardButtonContainerClick}
      >
        <div className={styles.button} />
        <div className={styles.dashboard}>Dashboard</div>
        <img
          className={styles.dashboardCircleStreamlineCIcon}
          loading="lazy"
          alt=""
          src="/dashboardcirclestreamlinecorepng@2x.png"
        />
      </div>
    </div>
  );
};

Content.propTypes = {
  className: PropTypes.string,

  /** Action props */
  onHive1ImageClick: PropTypes.func,
};

export default Content;
