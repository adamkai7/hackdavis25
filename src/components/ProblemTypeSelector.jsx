import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProblemTypeSelector = ({ topic, onProblemTypeChange }) => {
  const [problemTypes, setProblemTypes] = useState([]);
  const [selectedType, setSelectedType] = useState('');
  
  useEffect(() => {
    console.log(`Fetching problem types for topic: ${topic}`);
    axios.get(`/api/problem-types?topic=${topic}`)
      .then(response => {
        console.log('Received problem types:', response.data);
        setProblemTypes(response.data);
        if (response.data.length > 0) {
          setSelectedType(response.data[0]);
          onProblemTypeChange(response.data[0]);
        }
      })
      .catch(error => {
        console.error('Error fetching problem types:', error);
      });
  }, [topic, onProblemTypeChange]);

  const handleChange = (e) => {
    setSelectedType(e.target.value);
    onProblemTypeChange(e.target.value);
  };

  return (
    <div className="filter-group">
      <label>Problem Type:</label>
      <select 
        value={selectedType} 
        onChange={handleChange}
      >
        {problemTypes.map(type => (
          <option key={type} value={type}>{type}</option>
        ))}
      </select>
    </div>
  );
};

export default ProblemTypeSelector;