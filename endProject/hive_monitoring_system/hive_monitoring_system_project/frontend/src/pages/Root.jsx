import React from 'react';
import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import Content from "../components/Content";
import AnalyticsButton from "../components/AnalyticsButton";
import AnalyticsButtons from "../components/AnalyticsButtons";
import styles from "./Root.module.css";

const Root = () => {
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

  return (
    <div className={styles.root}>
      <div className={styles.main}>
        <div className={styles.rectangleParent}>
          <div className={styles.frameChild} />
          <Content />
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
          <AnalyticsButton
            analytics="Products"
            analyticsGraphStreamlineU="/motionsensorstreamlineultimatepng@2x.png"
            onAnalyticsButtonContainerClick={onModulesButtonContainerClick}
          />
          <AnalyticsButtons
            apiary="Profile"
            honeyCombStreamlineCyberp="/userprofilefocusstreamlinecoreremixpng@2x.png"
            onApiaryButtonContainerClick={onProfileButtonContainerClick}
          />
          <AnalyticsButton
            analytics="Logout"
            analyticsGraphStreamlineU="/logout3streamlinecorepng@2x.png"
            onAnalyticsButtonContainerClick={onLogoutButtonContainerClick}
          />
        </div>
      </div>
      <section className={styles.background} />
    </div>
  );
};

export default Root;
