import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import Content from "../components/Content";
import AnalyticsButton from "../components/AnalyticsButton";
import AnalyticsButtons from "../components/AnalyticsButtons";
import AnalyticsButtons1 from "../components/AnalyticsButtons1";
import styles from "./Root1.module.css";

const Root1 = () => {
  const navigate = useNavigate();

  const onHive1ImageClick = useCallback(() => {
    navigate("/");
  }, [navigate]);

  const onAnalyticsButtonContainerClick = useCallback(() => {
    navigate("/analytics-frame");
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

  const onApiarySaveButtonContainerClick = useCallback(() => {
    navigate("/apiary-frame-with-hives");
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
      <main className={styles.apiaryInfo}>
        <div className={styles.apiaryInfoChild} />
        <div className={styles.apiaryTitle}>
          <a className={styles.apiary}>Apiary</a>
        </div>
        <div className={styles.hiveCount}>
          <div className={styles.amountOfHives}>Amount of hives</div>
          <div className={styles.hiveCountInput}>
            <div className={styles.numberOfHivesTextbox} />
          </div>
        </div>
        <div className={styles.location}>
          <div className={styles.coordinates}>
            <div className={styles.latitude}>Latitude</div>
            <div className={styles.longitudeInput}>
              <div className={styles.longitude}>Longitude</div>
              <div
                className={styles.apiarySaveButton}
                onClick={onApiarySaveButtonContainerClick}
              >
                <div className={styles.button} />
                <div className={styles.save}>Save</div>
              </div>
            </div>
          </div>
          <div className={styles.inputDuplicate}>
            <div className={styles.inputPair}>
              <div className={styles.numberOfHivesTextbox1} />
              <div className={styles.numberOfHivesTextbox2} />
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Root1;
