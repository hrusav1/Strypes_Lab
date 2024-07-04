import { TextField, InputAdornment, Icon, IconButton } from "@mui/material";
import Navigation from "./Navigation";
import PropTypes from "prop-types";
import styles from "./FormContainer.module.css";

const FormContainer = ({ className = "" }) => {
  return (
    <div className={[styles.formContainer, className].join(" ")}>
      <div className={styles.loginForm} />
      <div className={styles.emailPasswordFields}>
        <TextField
          className={styles.email}
          placeholder="E-mail:"
          variant="outlined"
          sx={{
            "& fieldset": { border: "none" },
            "& .MuiInputBase-root": { height: "52px", backgroundColor: "#fff" },
            "& .MuiInputBase-input": { color: "#fff" },
            width: "208px",
          }}
        />
        <div className={styles.confirmPasswordWrapper}>
          <TextField
            className={styles.confirmPassword}
            placeholder="Username:"
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
        </div>
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
      </div>
      <div className={styles.usernameWrapper}>
        <TextField
          className={styles.username}
          placeholder="Confirm Password:"
          variant="outlined"
          sx={{
            "& fieldset": { border: "none" },
            "& .MuiInputBase-root": {
              height: "51.8px",
              backgroundColor: "#fff",
            },
            "& .MuiInputBase-input": { color: "#fff" },
            width: "208px",
          }}
        />
      </div>
      <Navigation login="Register" />
    </div>
  );
};

FormContainer.propTypes = {
  className: PropTypes.string,
};

export default FormContainer;
