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
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      tableData: []
    }
  },
  mounted() {
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
  }
}
</script>
