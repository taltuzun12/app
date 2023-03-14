<template>
  <div>
    <h1>Table Data</h1>
    <table>
      <thead>
        <tr>
          <th>Column 1</th>
          <th>Column 2</th>
          <th>Column 3</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in tableData" :key="index">
          <td>{{ item.column1 }}</td>
          <td>{{ item.column2 }}</td>
          <td>{{ item.column3 }}</td>
        </tr>
      </tbody>
    </table>
    
    <form @submit.prevent="insertData">
      <div>
        <label for="column1">Column 1:</label>
        <input type="text" id="column1" v-model="newData.column1">
      </div>
      <div>
        <label for="column2">Column 2:</label>
        <input type="text" id="column2" v-model="newData.column2">
      </div>
      <div>
        <label for="column3">Column 3:</label>
        <input type="text" id="column3" v-model="newData.column3">
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
        column1: '',
        column2: '',
        column3: ''
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
              column1: item[0],
              column2: item[1],
              column3: item[2]
            };
          });
        })
        .catch(error => {
          console.log(error);
        });
    },
    insertData() {
      axios.post('http://localhost:5000/api/data', this.newData)
        .then(response => {
          console.log(response.data);
          this.tableData.push(this.newData);
          this.newData = {
            column1: '',
            column2: '',
            column3: ''
          };
        })
        .catch(error => {
          console.log(error);
        });


     
    }
  }
}
</script>
