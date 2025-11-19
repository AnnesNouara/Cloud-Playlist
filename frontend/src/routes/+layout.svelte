<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';

	import { onMount } from 'svelte';

	// Browser used to test if client or server side
	import { browser } from '$app/environment';
	import 'bootstrap/dist/css/bootstrap.min.css';
	import 'bootstrap-icons/font/bootstrap-icons.min.css';

	onMount(async () => {
		if (browser) {
			// if running in browser, load bootstrap
			await import('bootstrap');
		}
	});

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<!-- Header with Navbar -->
<header class="navbar navbar-expand-md navbar-dark bd-navbar bg-dark">
  <nav class="container-xl flex-wrap flex-md-nowrap" aria-label="Main navigation">
		<div class="container-fluid main-wrapper">
			<a class="navbar-brand" href="/">
				<i class="bi bi-music-note me-2"></i>Cloud playlist App
			</a>
			<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#bdNavbar" aria-controls="bdNavbar" aria-expanded="false" aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>

			<div class="collapse navbar-collapse" id="navbarNav">
				<ul class="navbar-nav me-auto">
					<li class="nav-item">
						<a class="nav-link active" href="/tracks"><i class="bi bi-eye"></i>Tracks</a>
					</li>
					<li class="nav-item">
						<a class="nav-link active" href="/tracks/create"><i class="bi bi-plus-circle"></i>Add Tracks</a>
					</li>
				</ul>
			</div>
		</div>
	</nav>
</header>
<div class="container-xl bd-gutter my-md-4 bd-layout">
  {@render children?.()}
</div>

<style>
</style>
