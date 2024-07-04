import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import Content from "../components/Content";
import AnalyticsButton from "../components/AnalyticsButton";
import AnalyticsButtons from "../components/AnalyticsButtons";
import AnalyticsButtons1 from "../components/AnalyticsButtons1";
import styles from "./Root3.module.css";

const Root3 = () => {
  const navigate = useNavigate();

  const onHive1ImageClick = useCallback(() => {
    navigate("/");
  }, [navigate]);

  const onApiaryButtonContainerClick = useCallback(() => {
    navigate("/apiary-frame");
  }, [navigate]);

  const onContactsButtonContainerClick = useCallback(() => {
    navigate("/contacts-frame");
  }, [navigate]);

  const onModulesButtonContainerClick = useCallback(() => {
    navigate("/products-frame");
  }, [navigate]);

  const onProfileButtonClick = useCallback(() => {
    navigate("/profile-frame");
  }, [navigate]);

  const onLogoutButtonContainerClick = useCallback(() => {
    navigate("/home-frame");
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
          <AnalyticsButton
            analytics="Products"
            analyticsGraphStreamlineU="/motionsensorstreamlineultimatepng@2x.png"
            onAnalyticsButtonContainerClick={onModulesButtonContainerClick}
          />
          <AnalyticsButtons1 onProfileButtonClick={onProfileButtonClick} />
          <AnalyticsButton
            analytics="Logout"
            analyticsGraphStreamlineU="/logout3streamlinecorepng@2x.png"
            onAnalyticsButtonContainerClick={onLogoutButtonContainerClick}
          />
        </div>
      </div>
      <div className={styles.rectangleGroup}>
        <div className={styles.frameItem} />
        <a className={styles.analytics}>Analytics</a>
        <section className={styles.frameWrapper}>
          <div className={styles.honeyProductionPredictionParent}>
            <div className={styles.honeyProductionPrediction}>
              Honey production prediction
            </div>
            <div className={styles.predictions}>
              <div className={styles.honeyProductionTextbox} />
            </div>
            <div className={styles.hiveHealthPrediction}>
              Hive health prediction
            </div>
            <div className={styles.predictions1}>
              <div className={styles.hiveHelathPredictionTextbox} />
            </div>
          </div>
        </section>
      </div>
    </div>
  );
};

export default Root3;
