// frontend/screens/OrderScreen.js

import React, { useState } from 'react';
import { View, Text, Button, TextInput, ScrollView } from 'react-native';

const OrderScreen = () => {
  const [bombSize, setBombSize] = useState('');
  const [powerLevel, setPowerLevel] = useState('');
  const [deliveryLocation, setDeliveryLocation] = useState('');
  const [paymentMethod, setPaymentMethod] = useState('');

  const handleOrder = () => {
    if (!bombSize || !powerLevel || !deliveryLocation || !paymentMethod) {
      alert('Please fill in all fields before placing an order');
      return;
    }

    // Logic to process the order and send it to the backend for further processing
    console.log('Order placed successfully!');
  };

  return (
    <ScrollView>
      <View>
        <Text>Select Bomb Size:</Text>
        <TextInput
          value={bombSize}
          onChangeText={setBombSize}
          placeholder="Enter bomb size"
        />
      </View>
      <View>
        <Text>Select Power Level:</Text>
        <TextInput
          value={powerLevel}
          onChangeText={setPowerLevel}
          placeholder="Enter power level"
        />
      </View>
      <View>
        <Text>Enter Delivery Location:</Text>
        <TextInput
          value={deliveryLocation}
          onChangeText={setDeliveryLocation}
          placeholder="Enter delivery location"
        />
      </View>
      <View>
        <Text>Select Payment Method:</Text>
        <TextInput
          value={paymentMethod}
          onChangeText={setPaymentMethod}
          placeholder="Enter payment method"
        />
      </View>
      <Button title="Place Order" onPress={handleOrder} />
    </ScrollView>
  );
};

export default OrderScreen;