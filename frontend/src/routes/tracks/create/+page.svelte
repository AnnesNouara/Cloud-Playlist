<script lang="ts">
  import { onMount } from 'svelte';

  const API_BASE = 'http://127.0.0.1:8000';

  type Track = {
    id: number;
    song_name: string;
    artist: string;
    duration: string;
  };

  let tracks: Track[] = [];
  let error: string | null = null;

  // form fields
  let song_name = '';
  let artist = '';
  let duration = '';

  async function createTrack() {
    error = null;

    try {
      const res = await fetch(`${API_BASE}/tracks`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ song_name, artist, duration })
      });

      if (!res.ok) {
        throw new Error(`Failed to create track (${res.status})`);
      }

      const newTrack: Track = await res.json();
      tracks = [...tracks, newTrack];

      // clear form
      song_name = '';
      artist = '';
      duration = '';
    } catch (err) {
      error = err instanceof Error ? err.message : 'Unknown error';
    }
  }

</script>

<main>
  <h1>Cloud Playlist Tracker</h1>

  {#if error}
    <p class="error">{error}</p>
  {/if}

  <section class="form-section">
    <h2>Add Track</h2>
    <form on:submit|preventDefault={createTrack}>
      <label>
        Song name
        <input bind:value={song_name} required />
      </label>

      <label>
        Artist
        <input bind:value={artist} required />
      </label>

      <label>
        Duration
        <input bind:value={duration} placeholder="e.g. 3M 49S" required />
      </label>

      <button type="submit">Add</button>
    </form>
  </section>

</main>

<style>
  main {
    max-width: 700px;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  }

  h1 {
    margin-bottom: 1.5rem;
    margin-right: 5em;
  }

  .form-section{
    margin-bottom: 1rem;
    
  }

  form {
    display: grid;
    max-width: 400px;
  }

  label {
    display: flex;
    flex-direction: column;
    font-size: 0.9rem;
  }

  input {
    padding: 0.4rem 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  button {
    margin-top: 0.5rem;
    padding: 0.5rem 0.9rem;
    border: none;
    border-radius: 4px;
    background: #2563eb;
    color: white;
    font-weight: 500;
    cursor: pointer;
  }

  button:hover {
    background: #1d4ed8;
  }

  .error {
    color: #b91c1c;
    margin-bottom: 1rem;
  }
</style>
