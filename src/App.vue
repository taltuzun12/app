<template>
  <div>
    <h1>Table Data</h1>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Age</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in tableData" :key="index">
          <td>{{ item.id }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.age }}</td>
        </tr>
      </tbody>
    </table>

    <form @submit.prevent="insertData">
      <div>
        <label for="id">ID:</label>
        <input type="text" id="id" v-model="newData.id">
      </div>
      <div>
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="newData.name">
      </div>
      <div>
        <label for="age">Age:</label>
        <input type="text" id="age" v-model="newData.age">
      </div>
      <button type="submit">Submit</button>
    </form>
    
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      tableData: [],
      newData: {
        id: '',
        name: '',
        age: ''
      }
    }
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      axios.get('http://localhost:5000/api/data')
        .then(response => {
          console.log(response.data);
          this.tableData = response.data.map(item => {
            return {
              id: item[0],
              name: item[1],
              age: item[2]
            };
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    insertData() {
      axios.post('http://localhost:5000/api/data', {
          id: this.newData.id,
          name: this.newData.name,
          age: this.newData.age
        })
        .then(response => {
          console.log(response.data);
          this.tableData.push({
            id: this.newData.id,
            name: this.newData.name,
            age: this.newData.age
          });
          this.newData = {
            id: '',
            name: '',
            age: ''
          };
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
}
</script>
