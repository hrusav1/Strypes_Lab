import PropTypes from "prop-types";
import styles from "./HumidityDetails.module.css";

const HumidityDetails = ({ className = "" }) => {
  return (
    <section className={[styles.humidityDetails, className].join(" ")}>
      <div className={styles.humidityWrapper}>
        <h1 className={styles.humidity}>Humidity %</h1>
      </div>
      <div className={styles.humidityValue}>
        <div className={styles.value}>100</div>
        <div className={styles.humidityUnit}>
          <img className={styles.unitIcon} alt="" src="/vector-62.svg" />
        </div>
      </div>
      <div className={styles.humidityValuesTitle}>
        <div className={styles.humidityNameValues}>
          <div className={styles.humidityTitleValues}>75</div>
          <div className={styles.humidityIconsValues}>
            <img
              className={styles.humidityIndicatorsIcon}
              alt=""
              src="/vector-63.svg"
            />
          </div>
        </div>
      </div>
      <div className={styles.humidityValuesTitle1}>
        <div className={styles.parent}>
          <div className={styles.div}>50</div>
          <div className={styles.vectorWrapper}>
            <img className={styles.vectorIcon} alt="" src="/vector-63.svg" />
          </div>
        </div>
      </div>
      <div className={styles.humidityValuesTitle2}>
        <div className={styles.group}>
          <div className={styles.div1}>25</div>
          <div className={styles.vectorContainer}>
            <img className={styles.vectorIcon1} alt="" src="/vector-63.svg" />
          </div>
        </div>
      </div>
      <div className={styles.humidityChart}>
        <div className={styles.chartContainer}>
          <div className={styles.chartContent}>
            <div className={styles.chartElements}>
              <div className={styles.chartLabel}>0</div>
              <div className={styles.labelPosition}>
                <div className={styles.labelCoordinates}>
                  <img
                    className={styles.coordinateXIcon}
                    loading="lazy"
                    alt=""
                    src="/vector-66.svg"
                  />
                  <img
                    className={styles.coordinateYIcon}
                    alt=""
                    src="/vector-67.svg"
                  />
                </div>
              </div>
              <div className={styles.chartBars}>
                <img
                  className={styles.barsIcon}
                  loading="lazy"
                  alt=""
                  src="/vector-66.svg"
                />
              </div>
              <div className={styles.chartBars1}>
                <img
                  className={styles.vectorIcon2}
                  loading="lazy"
                  alt=""
                  src="/vector-66.svg"
                />
              </div>
              <div className={styles.chartBars2}>
                <img
                  className={styles.vectorIcon3}
                  loading="lazy"
                  alt=""
                  src="/vector-66.svg"
                />
              </div>
              <div className={styles.chartBars3}>
                <img
                  className={styles.vectorIcon4}
                  loading="lazy"
                  alt=""
                  src="/vector-66.svg"
                />
              </div>
              <div className={styles.chartBars4}>
                <img
                  className={styles.vectorIcon5}
                  loading="lazy"
                  alt=""
                  src="/vector-72.svg"
                />
              </div>
              <div className={styles.chartBars5}>
                <img
                  className={styles.vectorIcon6}
                  loading="lazy"
                  alt=""
                  src="/vector-73.svg"
                />
              </div>
              <div className={styles.chartBars6}>
                <img
                  className={styles.vectorIcon7}
                  alt=""
                  src="/vector-74.svg"
                />
              </div>
              <div className={styles.chartBars7}>
                <img
                  className={styles.vectorIcon8}
                  alt=""
                  src="/vector-75.svg"
                />
              </div>
              <div className={styles.chartBars8}>
                <img
                  className={styles.vectorIcon9}
                  alt=""
                  src="/vector-75.svg"
                />
              </div>
              <div className={styles.chartBars9}>
                <img
                  className={styles.vectorIcon10}
                  alt=""
                  src="/vector-74.svg"
                />
              </div>
              <div className={styles.chartBars10}>
                <img
                  className={styles.vectorIcon11}
                  alt=""
                  src="/vector-75.svg"
                />
              </div>
              <div className={styles.chartBars11}>
                <img
                  className={styles.vectorIcon12}
                  alt=""
                  src="/vector-79.svg"
                />
              </div>
              <div className={styles.chartBars12}>
                <img
                  className={styles.vectorIcon13}
                  alt=""
                  src="/vector-79.svg"
                />
              </div>
              <div className={styles.chartBars13}>
                <img
                  className={styles.vectorIcon14}
                  alt=""
                  src="/vector-75.svg"
                />
              </div>
              <div className={styles.chartBars14}>
                <img
                  className={styles.vectorIcon15}
                  alt=""
                  src="/vector-73.svg"
                />
              </div>
              <div className={styles.chartBars15}>
                <img
                  className={styles.vectorIcon16}
                  alt=""
                  src="/vector-75.svg"
                />
              </div>
              <div className={styles.chartBars16}>
                <img
                  className={styles.vectorIcon17}
                  alt=""
                  src="/vector-75.svg"
                />
              </div>
              <div className={styles.chartBars17}>
                <img
                  className={styles.vectorIcon18}
                  alt=""
                  src="/vector-79.svg"
                />
              </div>
              <div className={styles.chartBars18}>
                <img
                  className={styles.vectorIcon19}
                  alt=""
                  src="/vector-75.svg"
                />
              </div>
              <div className={styles.chartBars19}>
                <img
                  className={styles.vectorIcon20}
                  alt=""
                  src="/vector-73.svg"
                />
              </div>
              <div className={styles.chartBars20}>
                <img
                  className={styles.vectorIcon21}
                  alt=""
                  src="/vector-75.svg"
                />
              </div>
              <div className={styles.chartBars21}>
                <img
                  className={styles.vectorIcon22}
                  alt=""
                  src="/vector-89.svg"
                />
              </div>
            </div>
          </div>
          <div className={styles.chartData}>
            <div className={styles.dataPoints}>0</div>
            <div className={styles.dataPoints1}>2</div>
            <div className={styles.dataPoints2}>4</div>
            <div className={styles.dataPoints3}>6</div>
            <div className={styles.dataPoints4}>
              <div className={styles.points}>8</div>
            </div>
            <div className={styles.dataPoints5}>
              <div className={styles.div2}>11</div>
            </div>
            <div className={styles.dataPoints6}>
              <div className={styles.div3}>15</div>
            </div>
            <div className={styles.dataPoints7}>
              <div className={styles.div4}>19</div>
            </div>
            <div className={styles.dataPoints8}>
              <div className={styles.div5}>23</div>
            </div>
            <div className={styles.dataPoints9}>
              <div className={styles.div6}>27</div>
            </div>
            <div className={styles.dataPoints10}>
              <div className={styles.div7}>31</div>
            </div>
            <div className={styles.dataPoints11}>
              <div className={styles.div8}>35</div>
            </div>
            <div className={styles.dataPoints12}>
              <div className={styles.div9}>39</div>
            </div>
            <div className={styles.dataPoints13}>
              <div className={styles.div10}>43</div>
            </div>
            <div className={styles.dataPoints14}>
              <div className={styles.div11}>47</div>
            </div>
            <div className={styles.dataPoints15}>
              <div className={styles.div12}>51</div>
            </div>
            <div className={styles.dataPoints16}>
              <div className={styles.div13}>55</div>
            </div>
            <div className={styles.dataPoints17}>
              <div className={styles.div14}>59</div>
            </div>
            <div className={styles.dataPoints18}>
              <div className={styles.div15}>63</div>
            </div>
            <div className={styles.dataPoints19}>
              <div className={styles.div16}>67</div>
            </div>
            <div className={styles.dataPoints20}>
              <div className={styles.div17}>71</div>
            </div>
            <div className={styles.dataPoints21}>
              <div className={styles.div18}>75</div>
            </div>
            <div className={styles.dataPoints22}>79</div>
          </div>
        </div>
      </div>
    </section>
  );
};

HumidityDetails.propTypes = {
  className: PropTypes.string,
};

export default HumidityDetails;
