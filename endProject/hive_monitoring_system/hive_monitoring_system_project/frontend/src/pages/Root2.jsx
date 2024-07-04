import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import Content from "../components/Content";
import AnalyticsButton from "../components/AnalyticsButton";
import AnalyticsButtons from "../components/AnalyticsButtons";
import AnalyticsButtons1 from "../components/AnalyticsButtons1";
import styles from "./Root2.module.css";

const Root2 = () => {
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

  const onEditApiaryButtonContainerClick = useCallback(() => {
    navigate("/apiary-frame");
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
      <main className={styles.rectangleGroup}>
        <div className={styles.frameItem} />
        <a className={styles.apiary}>Apiary</a>
        <section className={styles.editApiaryButtonWrapper}>
          <div
            className={styles.editApiaryButton}
            onClick={onEditApiaryButtonContainerClick}
          >
            <div className={styles.button} />
            <div className={styles.editApiary}>Edit apiary</div>
          </div>
        </section>
      </main>
    </div>
  );
};

export default Root2;
