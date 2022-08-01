import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';
import ExamResult from './components/ExamResult';
import Home from './components/Home';
import RecordPage from './components/RecordPage';

const App = () => {
  return (
    <div className="App" id="App">
      <div className="header_container">
        <img src="/assets/Icon.svg" alt="logo" />
      </div>
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route exact path="/result" element={<ExamResult />} />
          <Route exact path="/record" element={<RecordPage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
};

export default App;
