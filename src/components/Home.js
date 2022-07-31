import React from 'react';
import ReactDOM from 'react-dom';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="home">
      <div className="text_container">
        <h1 className="home_title">Quick Ocular Measurements</h1>
        <p className="home_text">
          For best results, please ensure the face is facing straight-forward.
          Follow the instruction and avoid moving eyes or blinking while
          measuring.
        </p>
      </div>

      <img className="home_img" src="/assets/landing.svg" alt="landing img" />

      <div className="buttons_container">
        <Link to="/record" style={{ textDecoration: 'none' }}>
          <div className="primary_btn">Start Recording</div>
        </Link>
      </div>
    </div>
  );
};

export default Home;
