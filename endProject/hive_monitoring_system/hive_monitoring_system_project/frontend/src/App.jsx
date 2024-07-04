import { useEffect } from "react";
import React from 'react'
import {
  Routes,
  Route,
  useNavigationType,
  useLocation,
} from "react-router-dom";
import Root from "./pages/Root";
import Root1 from "./pages/Root1";
import Root2 from "./pages/Root2";
import Root3 from "./pages/Root3";
import Root4 from "./pages/Root4";
import Root5 from "./pages/Root5";
import Root6 from "./pages/Root6";
import Page from "./pages/Page";
import Root7 from "./pages/Root7";
import Root8 from "./pages/Root8";
import Root9 from "./pages/Root9";
import Root10 from "./pages/Root10";

function App() {
  console.log("App component is rendering");
  const action = useNavigationType();
  const location = useLocation();
  const pathname = location.pathname;

  useEffect(() => {
    if (action !== "POP") {
      window.scrollTo(0, 0);
    }
  }, [action, pathname]);

  useEffect(() => {
    let title = "";
    let metaDescription = "";

    switch (pathname) {
      case "/":
        title = "";
        metaDescription = "";
        break;
      case "/apiary-frame":
        title = "";
        metaDescription = "";
        break;
      case "/apiary-frame-with-hives":
        title = "";
        metaDescription = "";
        break;
      case "/analytics-frame":
        title = "";
        metaDescription = "";
        break;
      case "/dashboard-frame":
        title = "";
        metaDescription = "";
        break;
      case "/home-frame":
        title = "";
        metaDescription = "";
        break;
      case "/login-frame":
        title = "";
        metaDescription = "";
        break;
      case "/reset-pass-frame":
        title = "";
        metaDescription = "";
        break;
      case "/profile-frame":
        title = "";
        metaDescription = "";
        break;
      case "/products-frame":
        title = "";
        metaDescription = "";
        break;
      case "/contacts-frame":
        title = "";
        metaDescription = "";
        break;
      case "/register-frame":
        title = "";
        metaDescription = "";
        break;
    }

    if (title) {
      document.title = title;
    }

    if (metaDescription) {
      const metaDescriptionTag = document.querySelector(
        'head > meta[name="description"]'
      );
      if (metaDescriptionTag) {
        metaDescriptionTag.content = metaDescription;
      }
    }
  }, [pathname]);

  return (
    <Routes>
      <Route path="/" element={<Root />} />
      <Route path="/apiary-frame" element={<Root1 />} />
      <Route path="/apiary-frame-with-hives" element={<Root2 />} />
      <Route path="/analytics-frame" element={<Root3 />} />
      <Route path="/dashboard-frame" element={<Root4 />} />
      <Route path="/home-frame" element={<Root5 />} />
      <Route path="/login-frame" element={<Root6 />} />
      <Route path="/reset-pass-frame" element={<Page />} />
      <Route path="/profile-frame" element={<Root7 />} />
      <Route path="/products-frame" element={<Root8 />} />
      <Route path="/contacts-frame" element={<Root9 />} />
      <Route path="/register-frame" element={<Root10 />} />
    </Routes>
  );
}
export default App;
