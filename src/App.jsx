import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import ProblemGenerator from './components/ProblemGenerator';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/problems" element={<ProblemGenerator />} />
    </Routes>
  );
}

export default App;