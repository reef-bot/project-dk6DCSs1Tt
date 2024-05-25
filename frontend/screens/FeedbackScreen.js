// frontend/screens/FeedbackScreen.js

import React, { useState } from 'react';
import { View, Text, TextInput, Button, Alert } from 'react-native';

const FeedbackScreen = () => {
  const [feedback, setFeedback] = useState('');

  const submitFeedback = () => {
    if (feedback.trim() === '') {
      Alert.alert('Error', 'Please enter your feedback.');
    } else {
      // Code to submit feedback to the backend
      Alert.alert('Success', 'Thank you for your feedback!');
      setFeedback('');
    }
  };

  return (
    <View>
      <Text style={{ fontSize: 20, fontWeight: 'bold', marginBottom: 10 }}>Provide Your Feedback:</Text>
      <TextInput
        style={{ height: 100, borderColor: 'gray', borderWidth: 1, padding: 10, marginBottom: 10 }}
        multiline
        numberOfLines={4}
        placeholder='Enter your feedback here'
        value={feedback}
        onChangeText={text => setFeedback(text)}
      />
      <Button title='Submit Feedback' onPress={submitFeedback} />
    </View>
  );
};

export default FeedbackScreen;