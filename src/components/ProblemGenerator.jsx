import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Navbar from './Navbar';
import ProblemTypeSelector from './ProblemTypeSelector';

const ProblemGenerator = () => {
  const [topic, setTopic] = useState('Algebra');
  const [problemType, setProblemType] = useState('Solve for x (Linear)');
  const [difficulty, setDifficulty] = useState('Medium');
  const [numProblems, setNumProblems] = useState(5);
  const [problems, setProblems] = useState([]);
  const [solutions, setSolutions] = useState([]);
  const [showSolutions, setShowSolutions] = useState(false);
  const [loading, setLoading] = useState(false);
  const [topics, setTopics] = useState([]);

  // Fetch available topics
  useEffect(() => {
    axios.get('/api/topics')
      .then(response => {
        setTopics(response.data);
      })
      .catch(error => {
        console.error('Error fetching topics:', error);
      });
  }, []);

  // Handle problem type changes from the selector component
  const handleProblemTypeChange = (newProblemType) => {
    console.log(`Problem type changed to: ${newProblemType}`);
    setProblemType(newProblemType);
  };

  const handleGenerateProblems = () => {
    setLoading(true);
    setShowSolutions(false);
    
    axios.post('/api/algebra', {
      problem_type: problemType,
      difficulty: difficulty,
      num_problems: numProblems,
      topic: topic
    })
      .then(response => {
        setProblems(response.data.problems);
        setSolutions(response.data.solutions);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error generating problems:', error);
        setLoading(false);
      });
  };

  return (
    <div className="problem-generator">
      <Navbar />
      <div className="container">
        <h1>Math Problem Generator</h1>
        <p>Generate custom math problems based on your preferences</p>
        
        <div className="filters">
          <div className="filter-group">
            <label>Topic:</label>
            <select 
              value={topic} 
              onChange={(e) => {
                setTopic(e.target.value);
              }}
            >
              {topics.map(t => (
                <option key={t} value={t}>{t}</option>
              ))}
            </select>
          </div>
          
          <ProblemTypeSelector 
            topic={topic} 
            onProblemTypeChange={handleProblemTypeChange} 
          />
          
          <div className="filter-group">
            <label>Difficulty:</label>
            <select value={difficulty} onChange={(e) => setDifficulty(e.target.value)}>
              <option value="Easy">Easy</option>
              <option value="Medium">Medium</option>
              <option value="Hard">Hard</option>
            </select>
          </div>
          
          <div className="filter-group">
            <label>Number of Problems:</label>
            <input 
              type="number" 
              min="1" 
              max="20" 
              value={numProblems} 
              onChange={(e) => setNumProblems(parseInt(e.target.value))} 
            />
          </div>
        </div>
        
        <button 
          className="btn primary-btn generate-btn" 
          onClick={handleGenerateProblems}
          disabled={loading}
        >
          {loading ? 'Generating...' : 'Generate Problems'}
        </button>
        
        {problems.length > 0 && (
          <div className="problems-container">
            <h2>Generated Problems</h2>
            <div className="problems-list">
              {problems.map((problem, index) => (
                <div key={index} className="problem-card">
                  <h3>Problem {index + 1}</h3>
                  <p>{problem}</p>
                </div>
              ))}
            </div>
            
            <button 
              className="btn secondary-btn" 
              onClick={() => setShowSolutions(!showSolutions)}
            >
              {showSolutions ? 'Hide Solutions' : 'Show Solutions'}
            </button>
            
            {showSolutions && (
              <div className="solutions-container">
                <h2>Solutions</h2>
                <div className="solutions-list">
                  {solutions.map((solution, index) => (
                    <div key={index} className="solution-card">
                      <h3>Solution {index + 1}</h3>
                      <p>{solution}</p>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default ProblemGenerator;