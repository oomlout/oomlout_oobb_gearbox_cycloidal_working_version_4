$fn = 50;
use <C:/gh/oomlout_oobb_gearbox_cycloidal_working_version_4/cycloid.scad>


difference() {
	union() {
		translate(v = [0, 0, -1.5000000000]) {
			linear_extrude(height = 3) {
				offset(r = -0.2500000000) {
					cycloid(lobe_number = 79, radius_offset = 0.7500000000, radius_pin = 1.5000000000);
				}
			}
		}
	}
	union() {
		translate(v = [8.0000000000, -18.0000000000, 4.5000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.5000000000);
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.8000000000);
						}
						translate(v = [0, 0, -1.7000000000]) {
							cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.9000000000);
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.5000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-8.0000000000, 18.0000000000, 4.5000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.5000000000);
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.8000000000);
						}
						translate(v = [0, 0, -1.7000000000]) {
							cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.9000000000);
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.5000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-8.0000000000, -18.0000000000, -4.5000000000]) {
			rotate(a = [0, 180, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.5000000000);
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.8000000000);
						}
						translate(v = [0, 0, -1.7000000000]) {
							cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.9000000000);
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.5000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [8.0000000000, 18.0000000000, -4.5000000000]) {
			rotate(a = [0, 180, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.5000000000);
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.8000000000);
						}
						translate(v = [0, 0, -1.7000000000]) {
							cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.9000000000);
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.5000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [5.3030000000, 5.3030000000, 4.5000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.5000000000);
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.8000000000);
						}
						translate(v = [0, 0, -1.7000000000]) {
							cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.9000000000);
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.5000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-5.3030000000, -5.3030000000, -4.5000000000]) {
			rotate(a = [0, 180, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.5000000000);
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.8000000000);
						}
						translate(v = [0, 0, -1.7000000000]) {
							cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.9000000000);
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.5000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [5.3030000000, 5.3030000000, 4.5000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.5000000000);
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.8000000000);
						}
						translate(v = [0, 0, -1.7000000000]) {
							cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.9000000000);
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.5000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-5.3030000000, -5.3030000000, -4.5000000000]) {
			rotate(a = [0, 180, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							rotate(a = [0, 0, 0]) {
								difference() {
									union() {
										linear_extrude(height = 2.5000000000) {
											polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
										}
									}
									union();
								}
							}
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.5000000000);
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.8000000000);
						}
						translate(v = [0, 0, -1.7000000000]) {
							cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.9000000000);
						}
						translate(v = [0, 0, -9.0000000000]) {
							cylinder(h = 9, r = 1.5000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, -2.0000000000]) {
			union() {
				difference() {
					cylinder(h = 4, r = 16.0000000000);
					cylinder(h = 4, r = 12.5000000000);
				}
				difference() {
					translate(v = [0, 0, -50]) {
						cylinder(h = 100, r = 14.7500000000);
					}
					translate(v = [0, 0, -50]) {
						cylinder(h = 100, r = 13.7500000000);
					}
				}
			}
		}
		translate(v = [15, 15, -50.0000000000]) {
			cylinder(h = 100, r = 2.0000000000);
		}
		translate(v = [-15, -15, -50.0000000000]) {
			cylinder(h = 100, r = 2.0000000000);
		}
		translate(v = [-15, 15, -50.0000000000]) {
			cylinder(h = 100, r = 2.0000000000);
		}
		translate(v = [15, -15, -50.0000000000]) {
			cylinder(h = 100, r = 2.0000000000);
		}
	}
}