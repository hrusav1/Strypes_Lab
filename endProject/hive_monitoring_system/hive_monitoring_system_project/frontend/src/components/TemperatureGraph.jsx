import PropTypes from "prop-types";
import styles from "./TemperatureGraph.module.css";

const TemperatureGraph = ({ className = "" }) => {
  return (
    <div className={[styles.temperatureGraph, className].join(" ")}>
      <div className={styles.weightChartParent}>
        <div className={styles.weightChart}>
          <div className={styles.weightTitle}>
            <div className={styles.weightLabel}>
              <div className={styles.weightValue}>80</div>
              <div className={styles.weightUnits}>
                <div className={styles.weightUnitValues}>60</div>
                <div className={styles.weightUnitValues1}>40</div>
                <div className={styles.weightUnitValues2}>20</div>
                <div className={styles.weightUnitValues3}>0</div>
              </div>
            </div>
            <div className={styles.weightGraph}>
              <img
                className={styles.vectorIcon}
                loading="lazy"
                alt=""
                src="/vector-2.svg"
              />
              <div className={styles.weightPoints}>
                <div className={styles.weightValues}>
                  <div className={styles.weightPoint}>
                    <div className={styles.weightValuePoint}>
                      <div className={styles.weightMark}>
                        <div className={styles.weightMarkers}>
                          <img
                            className={styles.weightDegreesIcon}
                            alt=""
                            src="/vector-3.svg"
                          />
                          <img
                            className={styles.weightDegreesIcon1}
                            alt=""
                            src="/vector-4.svg"
                          />
                          <img
                            className={styles.weightDegreesIcon2}
                            alt=""
                            src="/vector-3.svg"
                          />
                        </div>
                      </div>
                      <img
                        className={styles.vectorIcon1}
                        loading="lazy"
                        alt=""
                        src="/vector-6.svg"
                      />
                    </div>
                    <img
                      className={styles.vectorIcon2}
                      loading="lazy"
                      alt=""
                      src="/vector-7.svg"
                    />
                  </div>
                  <div className={styles.weightScale}>
                    <div className={styles.weightScaleValues}>
                      <img
                        className={styles.vectorIcon3}
                        loading="lazy"
                        alt=""
                        src="/vector-2.svg"
                      />
                      <img
                        className={styles.weightScaleEnd}
                        alt=""
                        src="/vector-9.svg"
                      />
                    </div>
                    <img
                      className={styles.vectorIcon4}
                      loading="lazy"
                      alt=""
                      src="/vector-2.svg"
                    />
                  </div>
                </div>
              </div>
              <div className={styles.weightSeparatorParent}>
                <img
                  className={styles.weightSeparatorIcon}
                  loading="lazy"
                  alt=""
                  src="/vector.svg"
                />
                <img className={styles.groupIcon} alt="" src="/group-1.svg" />
              </div>
            </div>
            <div className={styles.weightName}>
              <img
                className={styles.weightIcons}
                loading="lazy"
                alt=""
                src="/vector-2.svg"
              />
            </div>
            <div className={styles.weightName1}>
              <img
                className={styles.vectorIcon5}
                loading="lazy"
                alt=""
                src="/vector-2.svg"
              />
            </div>
          </div>
        </div>
        <div className={styles.humidityChartParent}>
          <div className={styles.humidityChart}>
            <div className={styles.humidityUnits}>
              <div className={styles.humidityUnitValues}>0</div>
              <div className={styles.humidityUnitValues1}>2</div>
              <div className={styles.humidityUnitValues2}>4</div>
              <div className={styles.humidityUnitValues3}>6</div>
              <div className={styles.humidityUnitValues4}>8</div>
            </div>
          </div>
          <div className={styles.humidityLabel}>
            <h1 className={styles.weightKg}>Weight kg</h1>
            <div className={styles.humidityGraph}>
              <div className={styles.humidityTitle}>
                <div className={styles.humidityValue}>
                  <div className={styles.humidityNumber}>800</div>
                  <div className={styles.humidityDecimals}>
                    <div className={styles.humidityDecimalValues}>600</div>
                    <div className={styles.humidityDecimalValues1}>400</div>
                    <div className={styles.humidityDecimalValues2}>200</div>
                    <div className={styles.humidityDecimalValues3}>0</div>
                  </div>
                </div>
                <div className={styles.humiditySeparatorParent}>
                  <img
                    className={styles.humiditySeparatorIcon}
                    loading="lazy"
                    alt=""
                    src="/vector-14.svg"
                  />
                  <div className={styles.humidityPoints}>
                    <div className={styles.humidityValues}>
                      <div className={styles.humidityPoint}>
                        <div className={styles.humidityValuePoint}>
                          <div className={styles.humidityMark}>
                            <div className={styles.humidityMarkers}>
                              <img
                                className={styles.humidityDegreesIcon}
                                alt=""
                                src="/vector-15.svg"
                              />
                              <img
                                className={styles.humidityDegreesIcon1}
                                alt=""
                                src="/vector-15.svg"
                              />
                              <img
                                className={styles.humidityDegreesIcon2}
                                alt=""
                                src="/vector-15.svg"
                              />
                            </div>
                          </div>
                          <img
                            className={styles.vectorIcon6}
                            loading="lazy"
                            alt=""
                            src="/vector-18.svg"
                          />
                        </div>
                        <img
                          className={styles.vectorIcon7}
                          loading="lazy"
                          alt=""
                          src="/vector-19.svg"
                        />
                      </div>
                      <div className={styles.humidityScale}>
                        <img
                          className={styles.vectorIcon8}
                          loading="lazy"
                          alt=""
                          src="/vector-14.svg"
                        />
                        <img
                          className={styles.humidityScaleEnd}
                          alt=""
                          src="/vector-21.svg"
                        />
                      </div>
                    </div>
                  </div>
                  <div className={styles.humidityTooltip}>
                    <img
                      className={styles.humidityVerticalSeparator}
                      loading="lazy"
                      alt=""
                      src="/vector.svg"
                    />
                    <img
                      className={styles.groupIcon1}
                      alt=""
                      src="/group-2.svg"
                    />
                  </div>
                </div>
                <div className={styles.humidityIcons}>
                  <img
                    className={styles.vectorIcon9}
                    loading="lazy"
                    alt=""
                    src="/vector-14.svg"
                  />
                </div>
                <div className={styles.humidityIcons1}>
                  <img
                    className={styles.vectorIcon10}
                    loading="lazy"
                    alt=""
                    src="/vector-14.svg"
                  />
                </div>
                <div className={styles.humidityIcons2}>
                  <img
                    className={styles.vectorIcon11}
                    loading="lazy"
                    alt=""
                    src="/vector-14.svg"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className={styles.temperaturePoints}>
        <div className={styles.temperatureValues}>
          <div className={styles.temperatureTicks}>
            <div className={styles.temperatureMarkers}>
              <img
                className={styles.temperatureDegreesIcon}
                alt=""
                src="/vector-26.svg"
              />
            </div>
            <div className={styles.placeholder}>11</div>
          </div>
          <div className={styles.vectorWrapper}>
            <img
              className={styles.vectorIcon12}
              loading="lazy"
              alt=""
              src="/vector-27.svg"
            />
          </div>
        </div>
      </div>
      <div className={styles.temperaturePoints1}>
        <div className={styles.frameParent}>
          <div className={styles.frameGroup}>
            <div className={styles.vectorContainer}>
              <img
                className={styles.vectorIcon13}
                alt=""
                src="/vector-28.svg"
              />
            </div>
            <div className={styles.div}>15</div>
          </div>
          <div className={styles.vectorFrame}>
            <img className={styles.vectorIcon14} alt="" src="/vector-29.svg" />
          </div>
        </div>
      </div>
      <div className={styles.temperaturePoints2}>
        <div className={styles.frameContainer}>
          <div className={styles.frameDiv}>
            <div className={styles.vectorWrapper1}>
              <img
                className={styles.vectorIcon15}
                alt=""
                src="/vector-30.svg"
              />
            </div>
            <div className={styles.div1}>19</div>
          </div>
          <div className={styles.vectorWrapper2}>
            <img className={styles.vectorIcon16} alt="" src="/vector-31.svg" />
          </div>
        </div>
      </div>
      <div className={styles.temperaturePoints3}>
        <div className={styles.frameParent1}>
          <div className={styles.frameParent2}>
            <div className={styles.vectorWrapper3}>
              <img
                className={styles.vectorIcon17}
                alt=""
                src="/vector-32.svg"
              />
            </div>
            <div className={styles.div2}>23</div>
          </div>
          <div className={styles.vectorWrapper4}>
            <img className={styles.vectorIcon18} alt="" src="/vector-33.svg" />
          </div>
        </div>
      </div>
      <div className={styles.temperaturePoints4}>
        <div className={styles.frameParent3}>
          <div className={styles.frameParent4}>
            <div className={styles.vectorWrapper5}>
              <img
                className={styles.vectorIcon19}
                alt=""
                src="/vector-32.svg"
              />
            </div>
            <div className={styles.div3}>27</div>
          </div>
          <div className={styles.vectorWrapper6}>
            <img className={styles.vectorIcon20} alt="" src="/vector-33.svg" />
          </div>
        </div>
      </div>
      <div className={styles.temperaturePoints5}>
        <div className={styles.frameParent5}>
          <div className={styles.frameParent6}>
            <div className={styles.vectorWrapper7}>
              <img
                className={styles.vectorIcon21}
                alt=""
                src="/vector-30.svg"
              />
            </div>
            <div className={styles.div4}>31</div>
          </div>
          <div className={styles.vectorWrapper8}>
            <img className={styles.vectorIcon22} alt="" src="/vector-31.svg" />
          </div>
        </div>
      </div>
      <div className={styles.temperaturePoints6}>
        <div className={styles.frameParent7}>
          <div className={styles.frameParent8}>
            <div className={styles.vectorWrapper9}>
              <img
                className={styles.vectorIcon23}
                alt=""
                src="/vector-32.svg"
              />
            </div>
            <div className={styles.div5}>35</div>
          </div>
          <div className={styles.vectorWrapper10}>
            <img className={styles.vectorIcon24} alt="" src="/vector-33.svg" />
          </div>
        </div>
      </div>
      <div className={styles.temperaturePoints7}>
        <div className={styles.frameParent9}>
          <div className={styles.frameParent10}>
            <div className={styles.vectorWrapper11}>
              <img
                className={styles.vectorIcon25}
                alt=""
                src="/vector-40.svg"
              />
            </div>
            <div className={styles.div6}>39</div>
          </div>
          <div className={styles.vectorWrapper12}>
            <img className={styles.vectorIcon26} alt="" src="/vector-41.svg" />
          </div>
        </div>
      </div>
      <div className={styles.temperaturePoints8}>
        <div className={styles.frameParent11}>
          <div className={styles.frameParent12}>
            <div className={styles.vectorWrapper13}>
              <img
                className={styles.vectorIcon27}
                alt=""
                src="/vector-40.svg"
              />
            </div>
            <div className={styles.div7}>43</div>
          </div>
          <div className={styles.vectorWrapper14}>
            <img className={styles.vectorIcon28} alt="" src="/vector-41.svg" />
          </div>
        </div>
      </div>
      <div className={styles.temperaturePoints9}>
        <div className={styles.frameParent13}>
          <div className={styles.frameParent14}>
            <div className={styles.vectorWrapper15}>
              <img
                className={styles.vectorIcon29}
                alt=""
                src="/vector-32.svg"
              />
            </div>
            <div className={styles.div8}>47</div>
          </div>
          <div className={styles.vectorWrapper16}>
            <img className={styles.vectorIcon30} alt="" src="/vector-33.svg" />
          </div>
        </div>
      </div>
      <div className={styles.temperaturePoints10}>
        <div className={styles.frameParent15}>
          <div className={styles.frameParent16}>
            <div className={styles.vectorWrapper17}>
              <img
                className={styles.vectorIcon31}
                alt=""
                src="/vector-28.svg"
              />
            </div>
            <div className={styles.div9}>51</div>
          </div>
          <div className={styles.vectorWrapper18}>
            <img className={styles.vectorIcon32} alt="" src="/vector-29.svg" />
          </div>
        </div>
      </div>
      <div className={styles.temperaturePoints11}>
        <div className={styles.frameParent17}>
          <div className={styles.frameParent18}>
            <div className={styles.vectorWrapper19}>
              <img
                className={styles.vectorIcon33}
                alt=""
                src="/vector-32.svg"
              />
            </div>
            <div className={styles.div10}>55</div>
          </div>
          <div className={styles.vectorWrapper20}>
            <img className={styles.vectorIcon34} alt="" src="/vector-33.svg" />
          </div>
        </div>
      </div>
      <div className={styles.temperaturePoints12}>
        <div className={styles.frameParent19}>
          <div className={styles.frameParent20}>
            <div className={styles.vectorWrapper21}>
              <img
                className={styles.vectorIcon35}
                alt=""
                src="/vector-32.svg"
              />
            </div>
            <div className={styles.div11}>59</div>
          </div>
          <div className={styles.vectorWrapper22}>
            <img className={styles.vectorIcon36} alt="" src="/vector-33.svg" />
          </div>
        </div>
      </div>
      <div className={styles.temperaturePoints13}>
        <div className={styles.frameParent21}>
          <div className={styles.frameParent22}>
            <div className={styles.vectorWrapper23}>
              <img
                className={styles.vectorIcon37}
                alt=""
                src="/vector-40.svg"
              />
            </div>
            <div className={styles.div12}>63</div>
          </div>
          <div className={styles.vectorWrapper24}>
            <img className={styles.vectorIcon38} alt="" src="/vector-41.svg" />
          </div>
        </div>
      </div>
      <div className={styles.temperaturePoints14}>
        <div className={styles.frameParent23}>
          <div className={styles.frameParent24}>
            <div className={styles.vectorWrapper25}>
              <img
                className={styles.vectorIcon39}
                alt=""
                src="/vector-32.svg"
              />
            </div>
            <div className={styles.div13}>67</div>
          </div>
          <div className={styles.vectorWrapper26}>
            <img className={styles.vectorIcon40} alt="" src="/vector-33.svg" />
          </div>
        </div>
      </div>
      <div className={styles.temperaturePoints15}>
        <div className={styles.frameParent25}>
          <div className={styles.frameParent26}>
            <div className={styles.vectorWrapper27}>
              <img
                className={styles.vectorIcon41}
                alt=""
                src="/vector-28.svg"
              />
            </div>
            <div className={styles.div14}>71</div>
          </div>
          <div className={styles.vectorWrapper28}>
            <img className={styles.vectorIcon42} alt="" src="/vector-29.svg" />
          </div>
        </div>
      </div>
      <div className={styles.temperaturePoints16}>
        <div className={styles.frameParent27}>
          <div className={styles.frameParent28}>
            <div className={styles.vectorWrapper29}>
              <img
                className={styles.vectorIcon43}
                alt=""
                src="/vector-32.svg"
              />
            </div>
            <div className={styles.div15}>75</div>
          </div>
          <div className={styles.vectorWrapper30}>
            <img className={styles.vectorIcon44} alt="" src="/vector-33.svg" />
          </div>
        </div>
      </div>
      <div className={styles.temperaturePoints17}>
        <div className={styles.parent}>
          <div className={styles.div16}>79</div>
          <img className={styles.vectorIcon45} alt="" src="/vector-60.svg" />
          <img className={styles.vectorIcon46} alt="" src="/vector-61.svg" />
        </div>
      </div>
    </div>
  );
};

TemperatureGraph.propTypes = {
  className: PropTypes.string,
};

export default TemperatureGraph;
