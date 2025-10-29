<script>
    import axios from 'axios';
    let pclass, sex, age, sibsp, parch, fare, embarked, title, ticket_len, ticket_prefix, cabin;
    let prediction = "";
    let error = "";
  
    const predict = async () => {
      try {
        error = "";
        const response = await axios.post("http://127.0.0.1:5000/predict", {
          Pclass: +pclass,
          Sex: +sex,
          Age: +age,
          SibSp: +sibsp,
          Parch: +parch,
          Fare: +fare,
          Embarked: +embarked,
          Title: +title,
          Ticket_Len: +ticket_len,
          Ticket_Prefix: +ticket_prefix,
          Cabin: +cabin,
        });
        prediction = response.data.result;
        console.log("Prediction:", prediction);
      } catch (err) {
        console.error("Error:", err);
        error = "An error occurred while making the prediction.";
        prediction = "";
      }
    };
  </script>
  
  <div class="max-w-2xl mx-auto p-6 bg-white rounded-lg shadow-md">
    <div>
      <h2 class="text-2xl font-bold mb-6 text-center text-gray-800">
        Titanic Survival Prediction
      </h2>
      <form on:submit|preventDefault={predict} class="space-y-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <input
            type="number"
            bind:value={pclass}
            placeholder="Passenger Class (1, 2, 3)"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <input
            type="number"
            bind:value={sex}
            placeholder="Sex (0: Male, 1: Female)"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <input
            type="number"
            bind:value={age}
            placeholder="Age"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <input
            type="number"
            bind:value={sibsp}
            placeholder="Siblings/Spouses Aboard"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <input
            type="number"
            bind:value={parch}
            placeholder="Parents/Children Aboard"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <input
            type="number"
            bind:value={fare}
            placeholder="Fare"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <input
            type="number"
            bind:value={embarked}
            placeholder="Embarked (0: Cherbourg, 1: Queenstown, 2: Southampton)"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <input
            type="number"
            bind:value={title}
            placeholder="Title (numeric)"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <input
            type="number"
            bind:value={ticket_len}
            placeholder="Ticket Length"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <input
            type="number"
            bind:value={ticket_prefix}
            placeholder="Ticket Prefix (numeric)"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <input
            type="number"
            bind:value={cabin}
            placeholder="Cabin (numeric)"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
        <button
          type="submit"
          class="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 transition duration-300"
          >Predict</button
        >
      </form>
  
      {#if error}
        <p class="mt-4 text-red-600">{error}</p>
      {:else if prediction}
        <p class="mt-4 text-lg font-semibold text-green-600">
          Prediction: <span class="text-purple-400 font-bold text-lg">{prediction}</span>
        </p>
      {/if}
    </div>
  </div>
  