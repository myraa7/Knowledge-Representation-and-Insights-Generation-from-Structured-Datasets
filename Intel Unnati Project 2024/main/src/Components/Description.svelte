<script>
  const descriptions = [
    { name: "pclass", desc: "Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd). Represents the socio-economic status of the passenger." },
    { name: "sex", desc: "Gender (male or female). Indicates the gender of the passenger." },
    { name: "age", desc: "Age in years. Represents the age of the passenger." },
    { name: "sibsp", desc: "Number of Siblings/Spouses Aboard. Indicates the number of siblings or spouses the passenger had aboard the Titanic." },
    { name: "parch", desc: "Number of Parents/Children Aboard. Indicates the number of parents or children the passenger had aboard the Titanic." },
    { name: "fare", desc: "Fare. The ticket fare paid by the passenger." },
    { name: "embarked", desc: "Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton). Indicates the port where the passenger boarded the Titanic." },
    { name: "survived", desc: "Survival (0 = No, 1 = Yes). Indicates whether the passenger survived or not." },
    { name: "name", desc: "Name of the passenger." },
    { name: "ticket", desc: "Ticket number of the passenger." },
    { name: "cabin", desc: "Cabin number of the passenger." }
  ];
</script>

<style>
  .scroll-container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 10px;
    overflow-x: auto;
    white-space: nowrap;
    padding: 10px;
    border: 1px solid #ccc;
  }
  .item {
    padding: 10px;
    background-color: hwb(266 51% 5%);
    border: 1px solid hsl(0, 3%, 51%);
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  .item strong {
    display: block;
    margin-bottom: 5px;
    text-transform: capitalize;
    color: hsl(249, 75%, 38%);
  }
</style>

<div class="scroll-container">
  {#each descriptions as { name, desc }}
    <div class="item">
      <strong>{name}:</strong> {desc}
    </div>
  {/each}
</div>
