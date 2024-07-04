import { TextField, InputAdornment, Icon, IconButton } from "@mui/material";
import Navigation from "./Navigation";
import PropTypes from "prop-types";
import styles from "./NewPasswordForm.module.css";

const NewPasswordForm = ({ className = "" }) => {
  return (
    <div className={[styles.newPasswordForm, className].join(" ")}>
      <div className={styles.resetPasswordForm} />
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
      <div className={styles.passwordMatch}>
        <TextField
          className={styles.newPassword}
          placeholder="New Password:"
          variant="outlined"
          sx={{
            "& fieldset": { border: "none" },
            "& .MuiInputBase-root": {
              height: "51.3px",
              backgroundColor: "#fff",
            },
            "& .MuiInputBase-input": { color: "#fff" },
            width: "208px",
          }}
        />
      </div>
      <div className={styles.passwordMatch1}>
        <TextField
          className={styles.confirmPassword}
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
      <Navigation login="Reset" />
    </div>
  );
};

NewPasswordForm.propTypes = {
  className: PropTypes.string,
};

export default NewPasswordForm;
