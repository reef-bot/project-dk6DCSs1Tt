// File: frontend/screens/HomeScreen.js

import React, { useState, useEffect } from 'react';
import { View, Text, Button, TextInput, ScrollView } from 'react-native';
import axios from 'axios';

const HomeScreen = () => {
  const [atomBombSize, setAtomBombSize] = useState('');
  const [powerLevel, setPowerLevel] = useState('');
  const [orderStatus, setOrderStatus] = useState('');
  
  const placeOrder = async () => {
    try {
      const response = await axios.post('http://your-backend-url/api/orders', {
        size: atomBombSize,
        power: powerLevel
      });
      
      setOrderStatus('Order placed successfully!');
    } catch (error) {
      setOrderStatus('Failed to place order. Please try again.');
    }
  };

  return (
    <ScrollView>
      <View>
        <Text>Customize Your Atom Bomb:</Text>
        <TextInput
          placeholder="Enter bomb size"
          onChangeText={text => setAtomBombSize(text)}
          value={atomBombSize}
        />
        <TextInput
          placeholder="Enter power level"
          onChangeText={text => setPowerLevel(text)}
          value={powerLevel}
        />
        <Button title="Place Order" onPress={placeOrder} />
        <Text>{orderStatus}</Text>
      </View>
    </ScrollView>
  );
};

export default HomeScreen;