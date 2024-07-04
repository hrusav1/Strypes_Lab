import { useCallback } from "react";
import { TextField, InputAdornment, Icon, IconButton } from "@mui/material";
import { useNavigate } from "react-router-dom";
import PropTypes from "prop-types";
import styles from "./Content1.module.css";

const Content1 = ({ className = "" }) => {
  const navigate = useNavigate();

  const onLoginButtonContainerClick = useCallback(() => {
    navigate("/");
  }, [navigate]);

  const onForgotPassButtonContainerClick = useCallback(() => {
    navigate("/reset-pass-frame");
  }, [navigate]);

  const onHomeButtonContainerClick = useCallback(() => {
    navigate("/home-frame");
  }, [navigate]);

  return (
    <div className={[styles.content, className].join(" ")}>
      <div className={styles.loginForm} />
      <TextField
        className={styles.username}
        placeholder="Username:"
        variant="outlined"
        sx={{
          "& fieldset": { border: "none" },
          "& .MuiInputBase-root": { height: "51.6px", backgroundColor: "#fff" },
          "& .MuiInputBase-input": { color: "#fff" },
          width: "208px",
        }}
      />
      <div className={styles.actions}>
        <div className={styles.buttons}>
          <TextField
            className={styles.password}
            placeholder="Password:"
            variant="outlined"
            sx={{
              "& fieldset": { border: "none" },
              "& .MuiInputBase-root": {
                height: "51.6px",
                backgroundColor: "#fff",
              },
              "& .MuiInputBase-input": { color: "#fff" },
              width: "208px",
            }}
          />
          <div className={styles.buttonSet}>
            <div
              className={styles.loginButton}
              onClick={onLoginButtonContainerClick}
            >
              <div className={styles.button}>
                <div className={styles.button1} />
                <div className={styles.login}>Login</div>
              </div>
            </div>
          </div>
          <div className={styles.buttonSet1}>
            <div
              className={styles.forgotPassButton}
              onClick={onForgotPassButtonContainerClick}
            >
              <div className={styles.button2} />
              <div className={styles.forgotpass}>Forgot Pass</div>
            </div>
          </div>
          <div className={styles.buttonSet2}>
            <div
              className={styles.homeButton}
              onClick={onHomeButtonContainerClick}
            >
              <div className={styles.button3} />
              <div className={styles.home}>Home</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

Content1.propTypes = {
  className: PropTypes.string,
};

export default Content1;
