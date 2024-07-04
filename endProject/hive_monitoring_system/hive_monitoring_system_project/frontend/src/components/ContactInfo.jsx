import PropTypes from "prop-types";
import styles from "./ContactInfo.module.css";

const ContactInfo = ({ className = "" }) => {
  return (
    <div className={[styles.contactInfo, className].join(" ")}>
      <div className={styles.contactItems}>
        <div className={styles.emailContainer}>
          <img
            className={styles.freeRemixcomputerDevicesgm}
            loading="lazy"
            alt=""
            src="/free-remixcomputer-devicesgmail.svg"
          />
        </div>
        <div className={styles.hrusavgmailcom}>hrusav@gmail.com</div>
      </div>
      <div className={styles.phoneContainer}>
        <img
          className={styles.phoneStreamlineUltimatepngIcon}
          loading="lazy"
          alt=""
          src="/phonestreamlineultimatepng@2x.png"
        />
        <div className={styles.phoneNumber}>
          <div className={styles.placeholder}>+359 886676659</div>
        </div>
      </div>
      <div className={styles.facebookContainer}>
        <img
          className={styles.facebookLogo1StreamlineUIcon}
          loading="lazy"
          alt=""
          src="/facebooklogo1streamlineultimatepng@2x.png"
        />
        <div className={styles.facebookName}>
          <div className={styles.hrusav}>hrusav</div>
        </div>
      </div>
    </div>
  );
};

ContactInfo.propTypes = {
  className: PropTypes.string,
};

export default ContactInfo;
