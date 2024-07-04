import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import Content from "../components/Content";
import AnalyticsButton from "../components/AnalyticsButton";
import AnalyticsButtons from "../components/AnalyticsButtons";
import AnalyticsButtons1 from "../components/AnalyticsButtons1";
import styles from "./Root7.module.css";

const Root7 = () => {
  const navigate = useNavigate();

  const onHive1ImageClick = useCallback(() => {
    navigate("/");
  }, [navigate]);

  const onAnalyticsButtonContainerClick = useCallback(() => {
    navigate("/analytics-frame");
  }, [navigate]);

  const onApiaryButtonContainerClick = useCallback(() => {
    navigate("/apiary-frame");
  }, [navigate]);

  const onContactsButtonContainerClick = useCallback(() => {
    navigate("/contacts-frame");
  }, [navigate]);

  const onLogoutButtonContainerClick = useCallback(() => {
    navigate("/home-frame");
  }, [navigate]);

  const onButtonClick = useCallback(() => {
    navigate("/products-frame");
  }, [navigate]);

  return (
    <div className={styles.root}>
      <div className={styles.rootInner}>
        <div className={styles.rectangleParent}>
          <div className={styles.frameChild} />
          <Content onHive1ImageClick={onHive1ImageClick} />
          <AnalyticsButton
            analytics="Analytics"
            analyticsGraphStreamlineU="/analyticsgraphstreamlineultimatepng@2x.png"
            onAnalyticsButtonContainerClick={onAnalyticsButtonContainerClick}
          />
          <AnalyticsButtons
            apiary="Apiary"
            honeyCombStreamlineCyberp="/honeycombstreamlinecyberpng@2x.png"
            onApiaryButtonContainerClick={onApiaryButtonContainerClick}
          />
          <AnalyticsButtons
            apiary="Contacts"
            honeyCombStreamlineCyberp="/contactphonebookstreamlineplumppng@2x.png"
            onApiaryButtonContainerClick={onContactsButtonContainerClick}
          />
          <div className={styles.modulesButton}>
            <div className={styles.button} onClick={onButtonClick} />
            <div className={styles.modules}>Products</div>
            <img
              className={styles.motionSensorStreamlineUltiIcon}
              loading="lazy"
              alt=""
              src="/motionsensorstreamlineultimatepng@2x.png"
            />
          </div>
          <AnalyticsButtons1 />
          <AnalyticsButton
            analytics="Logout"
            analyticsGraphStreamlineU="/logout3streamlinecorepng@2x.png"
            onAnalyticsButtonContainerClick={onLogoutButtonContainerClick}
          />
        </div>
      </div>
      <main className={styles.rectangleGroup}>
        <div className={styles.frameItem} />
        <a className={styles.profile}>Profile</a>
      </main>
    </div>
  );
};

export default Root7;
