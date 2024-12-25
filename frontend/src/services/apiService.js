// frontend/src/services/apiService.js

import axios from 'axios';

// Define the base URL of the backend (ensure the backend is running on this address)
const API_URL = 'http://localhost:8000/generate_response/';

// Function to send query to the backend and get the response
export const fetchResponse = async (query) => {
  try {
    const response = await axios.post(API_URL, { query });
    return response.data.response; // Return the response data from the backend
  } catch (error) {
    // If there is an error, return an error message
    console.error('Error fetching response:', error);
    return 'Error retrieving response. Please try again.';
  }
};
