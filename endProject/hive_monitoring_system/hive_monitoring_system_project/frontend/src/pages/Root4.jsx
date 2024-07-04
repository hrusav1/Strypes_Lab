import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import AnalyticsButton1 from "../components/AnalyticsButton1";
import Actions from "../components/Actions";
import TemperatureGraph from "../components/TemperatureGraph";
import HumidityDetails from "../components/HumidityDetails";
import styles from "./Root4.module.css";

const Root4 = () => {
  const navigate = useNavigate();

  const onAnalyticsButtonContainerClick = useCallback(() => {
    navigate("/analytics-frame");
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

  const onProfileButtonContainerClick = useCallback(() => {
    navigate("/profile-frame");
  }, [navigate]);

  const onLogoutButtonContainerClick = useCallback(() => {
    navigate("/home-frame");
  }, [navigate]);

  const onHive1ImageClick = useCallback(() => {
    navigate("/");
  }, [navigate]);

  return (
    <div className={styles.root}>
      <div className={styles.rootInner}>
        <div className={styles.rectangleParent}>
          <div className={styles.frameChild} />
          <div className={styles.content}>
            <div className={styles.map}>
              <img
                className={styles.hive1Icon}
                loading="lazy"
                alt=""
                src="/hive-1@2x.png"
                onClick={onHive1ImageClick}
              />
            </div>
            <div className={styles.dashboardButton}>
              <div className={styles.button} />
              <h1 className={styles.dashboard}>Dashboard</h1>
              <img
                className={styles.dashboardCircleStreamlineCIcon}
                loading="lazy"
                alt=""
                src="/dashboardcirclestreamlinecorepng@2x.png"
              />
            </div>
          </div>
          <AnalyticsButton1
            analytics="Analytics"
            analyticsGraphStreamlineU="/analyticsgraphstreamlineultimatepng@2x.png"
            onAnalyticsButtonContainerClick={onAnalyticsButtonContainerClick}
          />
          <Actions
            apiary="Apiary"
            honeyCombStreamlineCyberp="/honeycombstreamlinecyberpng@2x.png"
            onApiaryButtonContainerClick={onApiaryButtonContainerClick}
          />
          <Actions
            apiary="Contacts"
            honeyCombStreamlineCyberp="/contactphonebookstreamlineplumppng@2x.png"
            onApiaryButtonContainerClick={onContactsButtonContainerClick}
          />
          <AnalyticsButton1
            analytics="Products"
            analyticsGraphStreamlineU="/motionsensorstreamlineultimatepng@2x.png"
            onAnalyticsButtonContainerClick={onModulesButtonContainerClick}
          />
          <Actions
            apiary="Profile"
            honeyCombStreamlineCyberp="/userprofilefocusstreamlinecoreremixpng@2x.png"
            onApiaryButtonContainerClick={onProfileButtonContainerClick}
          />
          <AnalyticsButton1
            analytics="Logout"
            analyticsGraphStreamlineU="/logout3streamlinecorepng@2x.png"
            onAnalyticsButtonContainerClick={onLogoutButtonContainerClick}
          />
        </div>
      </div>
      <main className={styles.header}>
        <div className={styles.headerChild} />
        <div className={styles.pageTitle}>
          <a className={styles.dashboard1}>Dashboard</a>
        </div>
        <section className={styles.headerIcons}>
          <img
            className={styles.notificationIcon}
            loading="lazy"
            alt=""
            src="/vector.svg"
          />
          <img
            className={styles.userIcon}
            loading="lazy"
            alt=""
            src="/vector-1.svg"
          />
          <img className={styles.groupIcon} alt="" src="/group.svg" />
        </section>
        <div className={styles.temperatureLabel}>
          <h1 className={styles.temperatureInC}>Temperature in C</h1>
        </div>
        <section className={styles.temperatureChart}>
          <TemperatureGraph />
          <div className={styles.parent}>
            <div className={styles.div}>0</div>
            <div className={styles.div1}>2</div>
            <div className={styles.div2}>4</div>
            <div className={styles.div3}>6</div>
            <div className={styles.wrapper}>
              <div className={styles.div4}>8</div>
            </div>
            <div className={styles.container}>
              <div className={styles.div5}>11</div>
            </div>
            <div className={styles.frame}>
              <div className={styles.div6}>15</div>
            </div>
            <div className={styles.frameDiv}>
              <div className={styles.div7}>19</div>
            </div>
            <div className={styles.wrapper1}>
              <div className={styles.div8}>23</div>
            </div>
            <div className={styles.wrapper2}>
              <div className={styles.div9}>27</div>
            </div>
            <div className={styles.wrapper3}>
              <div className={styles.div10}>31</div>
            </div>
            <div className={styles.wrapper4}>
              <div className={styles.div11}>35</div>
            </div>
            <div className={styles.wrapper5}>
              <div className={styles.div12}>39</div>
            </div>
            <div className={styles.wrapper6}>
              <div className={styles.div13}>43</div>
            </div>
            <div className={styles.wrapper7}>
              <div className={styles.div14}>47</div>
            </div>
            <div className={styles.wrapper8}>
              <div className={styles.div15}>51</div>
            </div>
            <div className={styles.wrapper9}>
              <div className={styles.div16}>55</div>
            </div>
            <div className={styles.wrapper10}>
              <div className={styles.div17}>59</div>
            </div>
            <div className={styles.wrapper11}>
              <div className={styles.div18}>63</div>
            </div>
            <div className={styles.wrapper12}>
              <div className={styles.div19}>67</div>
            </div>
            <div className={styles.wrapper13}>
              <div className={styles.div20}>71</div>
            </div>
            <div className={styles.wrapper14}>
              <div className={styles.div21}>75</div>
            </div>
            <div className={styles.div22}>79</div>
          </div>
        </section>
        <HumidityDetails />
      </main>
    </div>
  );
};

export default Root4;
