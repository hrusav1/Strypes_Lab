import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import PropTypes from "prop-types";
import styles from "./Actions.module.css";

const Actions = ({
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
    <div className={[styles.actions, className].join(" ")}>
      <div
        className={styles.apiaryButton}
        onClick={onApiaryButtonContainerClick}
      >
        <div className={styles.button} />
        <h1 className={styles.apiary}>{apiary}</h1>
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

Actions.propTypes = {
  className: PropTypes.string,
  apiary: PropTypes.string,
  honeyCombStreamlineCyberp: PropTypes.string,

  /** Action props */
  onApiaryButtonContainerClick: PropTypes.func,
};

export default Actions;
